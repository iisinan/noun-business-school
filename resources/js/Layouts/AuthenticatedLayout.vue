<script setup>
import { ref } from 'vue';
import ApplicationLogo from '@/Components/ApplicationLogo.vue';
import Dropdown from '@/Components/Dropdown.vue';
import DropdownLink from '@/Components/DropdownLink.vue';
import NavLink from '@/Components/NavLink.vue';
import ResponsiveNavLink from '@/Components/ResponsiveNavLink.vue';
import { Link } from '@inertiajs/vue3';

const showingNavigationDropdown = ref(false);
</script>

<template>
    <div>
        <div class="min-h-screen bg-gray-50">
            <nav class="bg-noun-dark shadow-lg">
                <!-- Primary Navigation Menu -->
                <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                    <div class="flex h-16 justify-between items-center">
                        <div class="flex items-center">
                            <!-- Logo -->
                            <div class="flex shrink-0 items-center">
                                <Link :href="route('dashboard')" class="flex items-center gap-3">
                                    <ApplicationLogo
                                        class="block h-8 w-auto fill-current text-noun-yellow"
                                    />
                                    <span class="text-white font-bold text-sm leading-tight hidden sm:block">
                                        NOUN<br><span class="text-noun-yellow font-normal text-xs">Business School</span>
                                    </span>
                                </Link>
                            </div>

                            <!-- Navigation Links -->
                            <div class="hidden space-x-1 sm:ms-10 sm:flex">
                                <NavLink
                                    :href="route('dashboard')"
                                    :active="route().current('dashboard') || route().current('admin.dashboard')"
                                >
                                    Dashboard
                                </NavLink>

                                <template v-if="$page.props.auth.user.role === 'admin'">
                                    <NavLink
                                        :href="route('admin.programmes.index')"
                                        :active="route().current('admin.programmes.*')"
                                    >
                                        Programmes
                                    </NavLink>
                                    <NavLink
                                        :href="route('admin.courses.index')"
                                        :active="route().current('admin.courses.*')"
                                    >
                                        Courses
                                    </NavLink>
                                    <NavLink
                                        :href="route('admin.applications.index')"
                                        :active="route().current('admin.applications.*')"
                                    >
                                        Applications
                                    </NavLink>
                                    <NavLink
                                        :href="route('admin.sessions.index')"
                                        :active="route().current('admin.sessions.*')"
                                    >
                                        Sessions
                                    </NavLink>
                                    <NavLink
                                        :href="route('admin.payments.index')"
                                        :active="route().current('admin.payments.*')"
                                    >
                                        Payments
                                    </NavLink>
                                    <NavLink
                                        :href="route('admin.results.upload')"
                                        :active="route().current('admin.results.*')"
                                    >
                                        Results
                                    </NavLink>
                                    <NavLink
                                        :href="route('admin.users.index')"
                                        :active="route().current('admin.users.*')"
                                    >
                                        Users
                                    </NavLink>
                                </template>

                                <template v-if="$page.props.auth.user.role === 'Student'">
                                    <NavLink
                                        :href="route('student.results')"
                                        :active="route().current('student.results')"
                                    >
                                        My Results
                                    </NavLink>
                                    <NavLink
                                        :href="route('student.payments')"
                                        :active="route().current('student.payments')"
                                    >
                                        Payments
                                    </NavLink>
                                </template>
                            </div>
                        </div>

                        <div class="hidden sm:ms-6 sm:flex sm:items-center gap-3">
                            <!-- User badge -->
                            <div class="text-right hidden md:block">
                                <div class="text-xs text-green-300">Welcome back</div>
                                <div class="text-sm font-medium text-white">{{ $page.props.auth.user.name }}</div>
                            </div>
                            <!-- Settings Dropdown -->
                            <div class="relative">
                                <Dropdown align="right" width="48">
                                    <template #trigger>
                                        <button
                                            type="button"
                                            class="flex items-center justify-center h-9 w-9 rounded-full bg-noun-green text-white font-bold text-sm hover:bg-green-600 transition ring-2 ring-noun-yellow focus:outline-none"
                                        >
                                            {{ $page.props.auth.user.name?.charAt(0)?.toUpperCase() }}
                                        </button>
                                    </template>

                                    <template #content>
                                        <DropdownLink
                                            :href="route('profile.edit')"
                                        >
                                            Profile
                                        </DropdownLink>
                                        <DropdownLink
                                            :href="route('logout')"
                                            method="post"
                                            as="button"
                                        >
                                            Log Out
                                        </DropdownLink>
                                    </template>
                                </Dropdown>
                            </div>
                        </div>

                        <!-- Hamburger -->
                        <div class="-me-2 flex items-center sm:hidden">
                            <button
                                @click="showingNavigationDropdown = !showingNavigationDropdown"
                                class="inline-flex items-center justify-center rounded-md p-2 text-green-200 transition duration-150 ease-in-out hover:bg-noun-green hover:text-white focus:bg-noun-green focus:text-white focus:outline-none"
                            >
                                <svg
                                    class="h-6 w-6"
                                    stroke="currentColor"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                >
                                    <path
                                        :class="{
                                            hidden: showingNavigationDropdown,
                                            'inline-flex': !showingNavigationDropdown,
                                        }"
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        stroke-width="2"
                                        d="M4 6h16M4 12h16M4 18h16"
                                    />
                                    <path
                                        :class="{
                                            hidden: !showingNavigationDropdown,
                                            'inline-flex': showingNavigationDropdown,
                                        }"
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        stroke-width="2"
                                        d="M6 18L18 6M6 6l12 12"
                                    />
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Responsive Navigation Menu -->
                <div
                    :class="{
                        block: showingNavigationDropdown,
                        hidden: !showingNavigationDropdown,
                    }"
                    class="sm:hidden border-t border-noun-green"
                >
                    <div class="space-y-1 pb-3 pt-2">
                        <ResponsiveNavLink
                            :href="route('dashboard')"
                            :active="route().current('dashboard')"
                        >
                            Dashboard
                        </ResponsiveNavLink>
                    </div>

                    <!-- Responsive Settings Options -->
                    <div class="border-t border-noun-green pb-1 pt-4">
                        <div class="px-4">
                            <div class="text-base font-medium text-white">
                                {{ $page.props.auth.user.name }}
                            </div>
                            <div class="text-sm font-medium text-green-300">
                                {{ $page.props.auth.user.email }}
                            </div>
                        </div>

                        <div class="mt-3 space-y-1">
                            <ResponsiveNavLink :href="route('profile.edit')">
                                Profile
                            </ResponsiveNavLink>
                            <ResponsiveNavLink
                                :href="route('logout')"
                                method="post"
                                as="button"
                            >
                                Log Out
                            </ResponsiveNavLink>
                        </div>
                    </div>
                </div>
            </nav>

            <!-- Page Heading -->
            <header
                class="bg-white border-b border-gray-200"
                v-if="$slots.header"
            >
                <div class="mx-auto max-w-7xl px-4 py-4 sm:px-6 lg:px-8 flex items-center gap-3">
                    <div class="w-1 h-6 bg-noun-green rounded-full"></div>
                    <slot name="header" />
                </div>
            </header>

            <!-- Page Content -->
            <main>
                <slot />
            </main>
        </div>
    </div>
</template>
