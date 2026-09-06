<script setup>
import { ref, computed } from 'vue';
import { Head } from '@inertiajs/vue3';
import StudentLayout from '@/Layouts/StudentLayout.vue';
import { useForm, usePage } from '@inertiajs/vue3';
import InputError from '@/Components/InputError.vue';
import TextInput from '@/Components/TextInput.vue';

const props = defineProps({
    wallet_balance: Number,
    transactions: { type: Array, default: () => [] },
    activeSession: Object,
    hasRegisteredSemester: Boolean,
    registeredCourses: { type: Array, default: () => [] },
    availableCourses: { type: Array, default: () => [] },
    studentSemester: { type: Number, default: 1 },
});

// ─── Toast system ──────────────────────────────────────────────
const toast = ref(null); // { type: 'success'|'error', message }
let toastTimer = null;
const showToast = (type, message) => {
    toast.value = { type, message };
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => { toast.value = null; }, 4000);
};

// ─── Confirmation modal ────────────────────────────────────────
const confirmModal = ref(null); // { title, body, onConfirm }
const openConfirm = (title, body, onConfirm) => {
    confirmModal.value = { title, body, onConfirm };
};
const doConfirm = () => {
    if (confirmModal.value?.onConfirm) confirmModal.value.onConfirm();
    confirmModal.value = null;
};

// ─── Forms ─────────────────────────────────────────────────────
const topupForm = useForm({ amount: '', type: 'WALLET_TOPUP' });
const semesterForm = useForm({});
const courseForm = useForm({ course_ids: [] });

const submitTopup = () => {
    if (!topupForm.amount || topupForm.amount < 1000) {
        showToast('error', 'Minimum top-up amount is NGN 1,000.');
        return;
    }
    topupForm.get(route('applicant.payment.initiate'));
};

const registerSemester = () => {
    openConfirm(
        'Semester Registration',
        'NGN 35,000 will be deducted from your wallet for the compulsory semester registration fee. This action cannot be undone.',
        () => {
            semesterForm.post(route('student.semester.register'), {
                onSuccess: () => showToast('success', 'Semester registration successful!'),
                onError: () => showToast('error', 'Failed to register. Please try again.'),
            });
        }
    );
};

const toggleCourse = (courseId) => {
    const index = courseForm.course_ids.indexOf(courseId);
    if (index === -1) courseForm.course_ids.push(courseId);
    else courseForm.course_ids.splice(index, 1);
};

const courseCost = (course) => course.units === 2 ? 2500 : (course.units === 3 ? 3500 : course.units * 1000);


const coreAvailableCourses = computed(() => {
    return props.availableCourses ? props.availableCourses.filter(c => c.type === 'Core' || !c.type) : [];
});
const electiveAvailableCourses = computed(() => {
    return props.availableCourses ? props.availableCourses.filter(c => c.type === 'Elective') : [];
});

const selectedElectivesCount = computed(() => {
    return electiveAvailableCourses.value.filter(c => courseForm.course_ids.includes(c.id)).length;
});

const calculateSelectedCost = computed(() => {
    if (!props.availableCourses) return 0;
    return props.availableCourses
        .filter(c => courseForm.course_ids.includes(c.id))
        .reduce((sum, c) => sum + courseCost(c), 0);
});

const canAffordSelection = computed(() => {
    return (props.wallet_balance || 0) >= calculateSelectedCost.value;
});

const registerCourses = () => {
    if (courseForm.course_ids.length === 0) {
        showToast('error', 'Please select at least one course to register.');
        return;
    }
    if (!canAffordSelection.value) {
        showToast('error', 'Insufficient wallet balance for the selected courses. Please top up first.');
        return;
    }
    if (!canRegisterMore.value) {
        showToast('error', `You cannot register more than ${MAX_CREDITS} units per semester.`);
        return;
    }
    openConfirm(
        'Course Registration',
        `NGN ${calculateSelectedCost.value.toLocaleString()} will be deducted from your wallet for ${courseForm.course_ids.length} selected course(s).`,
        () => {
            courseForm.post(route('student.courses.register'), {
                onSuccess: () => {
                    courseForm.course_ids = [];
                    showToast('success', 'Courses registered successfully!');
                },
                onError: () => showToast('error', 'Failed to register courses. Please try again.'),
            });
        }
    );
};

// ─── Derived stats ─────────────────────────────────────────────
const totalRegisteredCredits = computed(() =>
    props.registeredCourses?.reduce((sum, c) => sum + c.units, 0) ?? 0
);

const MAX_CREDITS = 24;

const totalSelectedCredits = computed(() => {
    let sum = 0;
    courseForm.course_ids.forEach(id => {
        const course = props.availableCourses.find(c => c.id === id);
        if (course) sum += course.units;
    });
    return sum;
});

const canRegisterMore = computed(() => {
    return (totalRegisteredCredits.value + totalSelectedCredits.value) <= MAX_CREDITS;
});

</script>

<template>
    <Head title="Course Registration" />
    <StudentLayout>
        <template #header>
            <h2 class="text-xl font-bold leading-tight text-noun-dark">Course Registration</h2>
        </template>
        
        <div class="py-8 px-4 sm:px-6 lg:px-8 ">
            <div class="space-y-6">

        <!-- Toast Notification -->
        <transition
            enter-active-class="transition duration-300 ease-out"
            enter-from-class="translate-y-2 opacity-0"
            enter-to-class="translate-y-0 opacity-100"
            leave-active-class="transition duration-200 ease-in"
            leave-from-class="translate-y-0 opacity-100"
            leave-to-class="translate-y-2 opacity-0"
        >
            <div v-if="toast" class="fixed bottom-6 right-6 z-50 max-w-sm w-full shadow-xl rounded-xl overflow-hidden pointer-events-none">
                <div
                    class="flex items-center gap-3 p-4 text-sm font-medium"
                    :class="toast.type === 'success' ? 'bg-emerald-600 text-white' : 'bg-red-600 text-white'"
                >
                    <svg v-if="toast.type === 'success'" class="w-5 h-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                    <svg v-else class="w-5 h-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z" /></svg>
                    {{ toast.message }}
                </div>
            </div>
        </transition>

        <!-- Confirm Modal -->
        <transition
            enter-active-class="transition duration-200 ease-out"
            enter-from-class="opacity-0"
            enter-to-class="opacity-100"
            leave-active-class="transition duration-150 ease-in"
            leave-from-class="opacity-100"
            leave-to-class="opacity-0"
        >
            <div v-if="confirmModal" class="fixed inset-0 z-50 flex items-center justify-center p-4">
                <div class="absolute inset-0 bg-black/40 backdrop-blur-sm" @click="confirmModal = null"></div>
                <div class="relative bg-white rounded-2xl shadow-2xl max-w-md w-full p-6 z-10">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="h-10 w-10 rounded-full bg-noun-light flex items-center justify-center flex-shrink-0">
                            <svg class="w-5 h-5 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900">{{ confirmModal.title }}</h3>
                    </div>
                    <p class="text-sm text-gray-600 leading-relaxed mb-6">{{ confirmModal.body }}</p>
                    <div class="flex gap-3 justify-end">
                        <button @click="confirmModal = null" class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200 transition">Cancel</button>
                        <button @click="doConfirm" class="px-4 py-2 text-sm font-bold text-white bg-noun-green rounded-lg hover:bg-noun-dark transition">Confirm & Pay</button>
                    </div>
                </div>
            </div>
        </transition>

        <!-- ── Section Title ── -->
        <div class="flex items-center gap-3">
            <div class="h-8 w-1 rounded-full bg-noun-green"></div>
            <h3 class="font-bold text-gray-800 text-xl">Student Portal</h3>
        </div>

        <!-- ── Stats Cards Row ── -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <!-- Wallet Balance Card -->
            <div class="bg-gradient-to-br from-noun-dark to-noun-green rounded-2xl p-5 text-white shadow-noun col-span-1 sm:col-span-1">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-green-300 text-xs font-semibold uppercase tracking-widest mb-1">Wallet Balance</p>
                        <p class="text-3xl font-black tracking-tight">₦{{ wallet_balance ? parseFloat(wallet_balance).toLocaleString() : '0' }}</p>
                    </div>
                    <div class="h-10 w-10 rounded-xl bg-white/10 flex items-center justify-center">
                        <svg class="w-5 h-5 text-noun-yellow" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" /></svg>
                    </div>
                </div>
                <form @submit.prevent="submitTopup" class="mt-4 flex gap-2">
                    <input
                        type="number"
                        v-model="topupForm.amount"
                        placeholder="Top-up amount"
                        min="1000"
                        class="flex-1 text-sm rounded-lg border-0 bg-white/15 text-white placeholder-green-300 focus:ring-2 focus:ring-noun-yellow px-3 py-2"
                    />
                    <button type="submit" :disabled="topupForm.processing" class="px-3 py-2 bg-noun-yellow text-noun-dark font-bold text-xs rounded-lg hover:bg-yellow-400 transition disabled:opacity-50 whitespace-nowrap">
                        Top Up
                    </button>
                </form>
            </div>

            <!-- Session Status Card -->
            <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-5">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-400 text-xs font-semibold uppercase tracking-widest mb-1">Active Session</p>
                        <p class="font-bold text-gray-900 text-lg leading-tight">{{ activeSession?.name ?? 'None' }}</p>
                    </div>
                    <div class="h-10 w-10 rounded-xl bg-blue-50 flex items-center justify-center">
                        <svg class="w-5 h-5 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
                    </div>
                </div>
                <div class="mt-3 flex items-center gap-2">
                    <span v-if="hasRegisteredSemester" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-emerald-100 text-emerald-700 text-xs font-bold">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                        Registered
                    </span>
                    <span v-else-if="activeSession" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-amber-100 text-amber-700 text-xs font-bold">
                        <span class="w-1.5 h-1.5 rounded-full bg-amber-500 animate-pulse"></span>
                        Pending Registration
                    </span>
                    <span v-if="activeSession" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-gray-100 text-gray-700 text-xs font-bold border border-gray-200">
                        Semester {{ studentSemester }}
                    </span>
                    <span v-else class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-gray-100 text-gray-500 text-xs font-bold">No Session</span>
                </div>
            </div>

            <!-- Credits Card -->
            <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-5">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-400 text-xs font-semibold uppercase tracking-widest mb-1">Registered Credits</p>
                        <p class="font-black text-gray-900 text-3xl">{{ totalRegisteredCredits }}</p>
                    </div>
                    <div class="h-10 w-10 rounded-xl bg-purple-50 flex items-center justify-center">
                        <svg class="w-5 h-5 text-purple-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg>
                    </div>
                </div>
                <p class="text-xs text-gray-400 mt-3">{{ registeredCourses?.length ?? 0 }} course(s) this semester</p>
            </div>
        </div>

        <!-- ── Main Grid ── -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div class="lg:col-span-2 space-y-5">

                <!-- ── Semester Registration ── -->
                <div class="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden">
                    <div class="px-6 py-4 border-b border-gray-100 flex items-center gap-3">
                        <div class="h-8 w-8 rounded-lg flex items-center justify-center" :class="hasRegisteredSemester ? 'bg-emerald-100' : 'bg-amber-100'">
                            <svg v-if="hasRegisteredSemester" class="w-4 h-4 text-emerald-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" /></svg>
                            <svg v-else class="w-4 h-4 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        </div>
                        <h3 class="text-base font-bold text-gray-900">Step 1 — Semester Registration</h3>
                    </div>
                    <div class="px-6 py-5">
                        <div v-if="!activeSession" class="text-center py-6 text-gray-400 text-sm">
                            <svg class="w-8 h-8 mx-auto mb-2 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
                            No active academic session available at this time.
                        </div>
                        <div v-else-if="hasRegisteredSemester" class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-5 p-4 bg-emerald-50 rounded-xl border border-emerald-200">
                            <div class="flex items-center gap-3">
                                <div class="h-10 w-10 rounded-full bg-emerald-600 flex items-center justify-center flex-shrink-0">
                                    <svg class="w-5 h-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" /></svg>
                                </div>
                                <div>
                                    <p class="font-bold text-emerald-800 text-sm">Registered for Semester {{ studentSemester }} ({{ activeSession.name }})</p>
                                    <p class="text-xs text-emerald-600 mt-0.5">Proceed to Course Registration below.</p>
                                </div>
                            </div>
                            

                        </div>
                        <div v-else class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-5 p-4 bg-amber-50 rounded-xl border border-amber-200">
                            <div>
                                <p class="font-bold text-gray-800 text-sm">{{ activeSession.name }} — Semester Fee</p>
                                <p class="text-xs text-gray-500 mt-0.5">Compulsory, deducted from your wallet</p>
                                <p class="text-xl font-black text-noun-dark mt-2">₦35,000</p>
                            </div>
                            <button
                                @click="registerSemester"
                                :disabled="semesterForm.processing || (wallet_balance ?? 0) < 35000"
                                class="flex-shrink-0 inline-flex items-center gap-2 px-5 py-2.5 bg-noun-green text-white font-bold text-sm rounded-xl hover:bg-noun-dark transition shadow-sm disabled:opacity-50 disabled:cursor-not-allowed"
                            >
                                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                                {{ semesterForm.processing ? 'Processing…' : 'Pay & Register' }}
                            </button>
                        </div>
                        <p v-if="!hasRegisteredSemester && activeSession && (wallet_balance ?? 0) < 35000" class="mt-3 text-xs text-red-600 font-medium flex items-center gap-1">
                            <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" /></svg>
                            Insufficient balance — please top up your wallet before registering.
                        </p>
                    </div>
                </div>

                <!-- ── Course Registration ── -->
                <div v-if="hasRegisteredSemester" class="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden">
                    <div class="px-6 py-4 border-b border-gray-100 flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <div class="h-8 w-8 rounded-lg bg-blue-100 flex items-center justify-center">
                                <svg class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg>
                            </div>
                            <h3 class="text-base font-bold text-gray-900">Step 2 — Course Registration</h3>
                        </div>
                        <a
                            v-if="registeredCourses && registeredCourses.length > 0"
                            :href="route('student.courses.slip')"
                            target="_blank"
                            class="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold text-noun-green border border-noun-green rounded-lg hover:bg-noun-light transition"
                        >
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
                            Print Slip
                        </a>
                    </div>

                    <div class="px-6 py-5 space-y-5">
                        <!-- Already-registered courses -->
                        <div v-if="registeredCourses && registeredCourses.length > 0">
                            <div class="flex items-center justify-between mb-3">
                                <p class="text-xs font-bold text-gray-400 uppercase tracking-wider">Registered Courses</p>
                                <span class="text-xs font-bold bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-md">{{ totalRegisteredCredits }} / {{ MAX_CREDITS }} Units</span>
                            </div>
                            
                            <!-- Credit Progress Bar -->
                            <div class="w-full bg-gray-200 rounded-full h-1.5 mb-4 overflow-hidden flex">
                                <div class="bg-noun-green h-1.5 transition-all" :style="{ width: Math.min((totalRegisteredCredits / MAX_CREDITS) * 100, 100) + '%' }"></div>
                                <div class="bg-noun-yellow h-1.5 transition-all opacity-70" :style="{ width: Math.min((totalSelectedCredits / MAX_CREDITS) * 100, 100 - ((totalRegisteredCredits / MAX_CREDITS) * 100)) + '%' }"></div>
                            </div>
                            <div class="space-y-2">
                                <div v-for="c in registeredCourses" :key="c.id" class="flex items-center justify-between py-2.5 px-4 bg-emerald-50 border border-emerald-100 rounded-xl">
                                    <div class="flex items-center gap-3">
                                        <div class="h-7 w-7 rounded-lg bg-emerald-600 flex items-center justify-center flex-shrink-0">
                                            <svg class="w-3.5 h-3.5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" /></svg>
                                        </div>
                                        <div>
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm font-bold text-gray-800">{{ c.code }}</span>
                                                <span 
                                                    v-if="c.type" 
                                                    class="px-1.5 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider" 
                                                    :class="c.type === 'Core' ? 'bg-indigo-100 text-indigo-700' : 'bg-emerald-200 text-emerald-800'"
                                                >
                                                    {{ c.type }}
                                                </span>
                                            </div>
                                            <span class="text-xs text-gray-500 block mt-0.5">{{ c.title }}</span>
                                        </div>
                                    </div>
                                    <span class="text-xs font-semibold text-gray-500 bg-white border border-gray-200 px-2 py-1 rounded-md">{{ c.units }} cr</span>
                                </div>
                            </div>
                        </div>

                        <!-- Available courses to register -->
                        <div v-if="availableCourses && availableCourses.length > 0">
                            
                            <div v-if="coreAvailableCourses.length > 0" class="mb-6">
                                <p class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3">Core Courses</p>
                                <div class="space-y-2">
                                    <label
                                        v-for="course in coreAvailableCourses"
                                        :key="course.id"
                                        class="flex items-center gap-4 py-3 px-4 rounded-xl border cursor-pointer transition-all"
                                        :class="courseForm.course_ids.includes(course.id)
                                            ? 'bg-blue-50 border-blue-300 shadow-sm'
                                            : 'bg-white border-gray-200 hover:border-blue-200 hover:bg-blue-50/50'"
                                    >
                                        <input
                                            type="checkbox"
                                            :value="course.id"
                                            :checked="courseForm.course_ids.includes(course.id)"
                                            @change="toggleCourse(course.id)"
                                            class="h-4 w-4 rounded border-gray-300 text-noun-green focus:ring-noun-green"
                                        />
                                        <div class="flex-1 min-w-0">
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm font-bold text-gray-800">{{ course.code }}</span>
                                                <span class="px-1.5 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider bg-indigo-100 text-indigo-700">CORE</span>
                                                <span class="hidden sm:inline text-sm text-gray-500 truncate">— {{ course.title }}</span>
                                            </div>
                                            <span class="sm:hidden text-xs text-gray-500 block mt-0.5 truncate">{{ course.title }}</span>
                                        </div>
                                        <div class="flex items-center gap-3 flex-shrink-0">
                                            <span class="text-xs text-gray-400 bg-gray-100 px-2 py-1 rounded-md font-medium">{{ course.units }} cr</span>
                                            <span class="text-sm font-bold text-gray-900">₦{{ courseCost(course).toLocaleString() }}</span>
                                        </div>
                                    </label>
                                </div>
                            </div>

                            <div v-if="electiveAvailableCourses.length > 0" class="mb-6">
                                <div class="flex items-center justify-between mb-3">
                                    <p class="text-xs font-bold text-gray-400 uppercase tracking-wider">Elective Courses</p>
                                    <p class="text-[10px] font-bold text-amber-500 uppercase tracking-wider bg-amber-50 px-2 py-0.5 rounded-full border border-amber-100">Choose Two</p>
                                </div>
                                <div class="space-y-2">
                                    <label
                                        v-for="course in electiveAvailableCourses"
                                        :key="course.id"
                                        class="flex items-center gap-4 py-3 px-4 rounded-xl border cursor-pointer transition-all"
                                        :class="courseForm.course_ids.includes(course.id)
                                            ? 'bg-blue-50 border-blue-300 shadow-sm'
                                            : 'bg-white border-gray-200 hover:border-blue-200 hover:bg-blue-50/50'"
                                    >
                                        <input
                                            type="checkbox"
                                            :value="course.id"
                                            :checked="courseForm.course_ids.includes(course.id)"
                                            @change="toggleCourse(course.id)"
                                            class="h-4 w-4 rounded border-gray-300 text-noun-green focus:ring-noun-green"
                                        />
                                        <div class="flex-1 min-w-0">
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm font-bold text-gray-800">{{ course.code }}</span>
                                                <span class="px-1.5 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider bg-amber-100 text-amber-700">ELECTIVE</span>
                                                <span class="hidden sm:inline text-sm text-gray-500 truncate">— {{ course.title }}</span>
                                            </div>
                                            <span class="sm:hidden text-xs text-gray-500 block mt-0.5 truncate">{{ course.title }}</span>
                                        </div>
                                        <div class="flex items-center gap-3 flex-shrink-0">
                                            <span class="text-xs text-gray-400 bg-gray-100 px-2 py-1 rounded-md font-medium">{{ course.units }} cr</span>
                                            <span class="text-sm font-bold text-gray-900">₦{{ courseCost(course).toLocaleString() }}</span>
                                        </div>
                                    </label>
                                </div>
                            </div>

                            <!-- Selection summary bar -->
                            <div class="mt-5 bg-noun-dark rounded-xl p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                                <div>
                                    <p class="text-green-300 text-xs font-semibold uppercase tracking-wider">Selection Total ({{ totalSelectedCredits }} units)</p>
                                    <p class="text-white font-black text-xl mt-0.5">₦{{ calculateSelectedCost.toLocaleString() }}</p>
                                    <p v-if="!canAffordSelection && courseForm.course_ids.length > 0" class="text-red-400 text-xs font-medium mt-1 flex items-center gap-1">
                                        <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" /></svg>
                                        Exceeds balance by ₦{{ (calculateSelectedCost - wallet_balance).toLocaleString() }}
                                    </p>
                                    <p v-if="selectedElectivesCount > 2" class="text-red-400 text-xs font-medium mt-1 flex items-center gap-1">
                                        <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" /></svg>
                                        You can only select up to 2 elective courses!
                                    </p>
                                    <p v-if="!canRegisterMore && courseForm.course_ids.length > 0" class="text-red-400 text-xs font-medium mt-1 flex items-center gap-1">
                                        <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" /></svg>
                                        Exceeds maximum {{ MAX_CREDITS }} units per semester!
                                    </p>
                                </div>
                                <button
                                    @click="registerCourses"
                                    :disabled="courseForm.processing || courseForm.course_ids.length === 0 || !canAffordSelection || !canRegisterMore || selectedElectivesCount > 2"
                                    class="flex-shrink-0 inline-flex items-center gap-2 px-5 py-2.5 bg-noun-yellow text-noun-dark font-bold text-sm rounded-xl hover:bg-yellow-400 transition disabled:opacity-50 disabled:cursor-not-allowed shadow-sm"
                                >
                                    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                                    {{ courseForm.processing ? 'Processing…' : `Register ${courseForm.course_ids.length > 0 ? courseForm.course_ids.length + ' Course(s)' : ''}` }}
                                </button>
                            </div>
                        </div>

                        <div v-else-if="registeredCourses && registeredCourses.length > 0" class="text-center py-6">
                            <div class="h-12 w-12 rounded-full bg-emerald-100 flex items-center justify-center mx-auto mb-3">
                                <svg class="w-6 h-6 text-emerald-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                            </div>
                            <p class="text-sm font-bold text-gray-700">All courses registered!</p>
                            <p class="text-xs text-gray-400 mt-1">You have registered for all available courses this semester.</p>
                        </div>

                        <div v-else class="text-center py-6 text-gray-400 text-sm">
                            No courses are available for registration in this session yet.
                        </div>
                    </div>
                </div>

                <!-- Step 2 locked hint -->
                <div v-else class="bg-white rounded-2xl border border-dashed border-gray-200 p-5 flex items-center gap-4 text-gray-400">
                    <div class="h-10 w-10 rounded-xl bg-gray-100 flex items-center justify-center flex-shrink-0">
                        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
                    </div>
                    <div>
                        <p class="text-sm font-bold text-gray-500">Step 2 — Course Registration</p>
                        <p class="text-xs mt-0.5">Complete semester registration above to unlock course selection.</p>
                    </div>
                </div>
            </div>

            <!-- ── Transactions Sidebar ── -->
            <div class="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden flex flex-col">
                <div class="px-5 py-4 border-b border-gray-100 flex items-center gap-2">
                    <svg class="w-4 h-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" /></svg>
                    <h3 class="text-sm font-bold text-gray-700 uppercase tracking-wide">Recent Transactions</h3>
                </div>

                <div v-if="!transactions || transactions.length === 0" class="flex-1 flex flex-col items-center justify-center p-8 text-center text-gray-400">
                    <svg class="w-10 h-10 mb-3 text-gray-200" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" /></svg>
                    <p class="text-sm font-medium">No transactions yet</p>
                    <p class="text-xs mt-1">Wallet activity will appear here.</p>
                </div>

                <ul v-else class="divide-y divide-gray-50 flex-1 overflow-y-auto max-h-96">
                    <li v-for="tx in transactions" :key="tx.id" class="px-5 py-3.5 hover:bg-gray-50 transition-colors">
                        <div class="flex items-start gap-3">
                            <div
                                class="h-8 w-8 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5"
                                :class="tx.amount > 0 ? 'bg-emerald-100' : 'bg-red-100'"
                            >
                                <svg v-if="tx.amount > 0" class="w-3.5 h-3.5 text-emerald-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M7 11l5-5m0 0l5 5m-5-5v12" /></svg>
                                <svg v-else class="w-3.5 h-3.5 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M17 13l-5 5m0 0l-5-5m5 5V6" /></svg>
                            </div>
                            <div class="flex-1 min-w-0">
                                <p class="text-xs font-semibold text-gray-800 leading-tight truncate">{{ tx.description }}</p>
                                <p class="text-xs text-gray-400 mt-0.5">{{ new Date(tx.created_at).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }) }}</p>
                            </div>
                            <span class="text-sm font-bold whitespace-nowrap" :class="tx.amount > 0 ? 'text-emerald-600' : 'text-red-500'">
                                {{ tx.amount > 0 ? '+' : '' }}₦{{ Math.abs(parseInt(tx.amount)).toLocaleString() }}
                            </span>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>

        </div>
    </StudentLayout>
</template>