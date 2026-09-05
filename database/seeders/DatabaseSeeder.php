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
    }
}
