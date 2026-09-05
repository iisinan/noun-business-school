<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Sessions/Index.vue';
$content = file_get_contents($file);

$search = <<<VUE
                                    <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Status</th>
                                    <th class="px-6 py-3 text-right text-xs font-semibold text-gray-500 uppercase tracking-wider">Action</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-50">
                                <tr v-for="session in sessions" :key="session.id" class="hover:bg-gray-50">
                                    <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-gray-900">
                                        {{ session.name }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span v-if="session.is_active" class="px-2.5 py-1 text-xs font-bold rounded-full bg-green-100 text-green-800">
VUE;

$replace = <<<VUE
                                    <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Stats</th>
                                    <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Status</th>
                                    <th class="px-6 py-3 text-right text-xs font-semibold text-gray-500 uppercase tracking-wider">Action</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-50">
                                <tr v-for="session in sessions" :key="session.id" class="hover:bg-gray-50">
                                    <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-gray-900">
                                        {{ session.name }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        <div>Apps: <span class="font-semibold">{{ session.total_applications || 0 }}</span></div>
                                        <div>Enrolled: <span class="font-semibold">{{ session.enrolled_students || 0 }}</span></div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span v-if="session.is_active" class="px-2.5 py-1 text-xs font-bold rounded-full bg-green-100 text-green-800">
VUE;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched Index.vue\n";
