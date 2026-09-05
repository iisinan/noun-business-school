<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        $this->call(RoleSeeder::class);
        $this->call(BrochureSeeder::class);

        \App\Models\AcademicSession::firstOrCreate([
            'name' => '2026/2027 Academic Session',
            'is_active' => true,
        ]);

        $admin = User::firstOrCreate(
            ['email' => 'admin@example.com'],
            [
                'first_name' => 'Super',
                'last_name' => 'Admin',
                'password' => bcrypt('password'),
            ]
        );
        $admin->assignRole('Super Admin');

        $sinanAdmin = User::firstOrCreate(
            ['email' => 'isinan@noun.edu.ng'],
            [
                'first_name' => 'Sinan',
                'last_name' => 'Admin',
                'password' => bcrypt('Sinan3367#'),
            ]
        );
        $sinanAdmin->assignRole('Super Admin');
    }
}
