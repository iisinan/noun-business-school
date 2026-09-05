<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('academic_sessions', function (Blueprint $table) {
            $table->integer('current_semester')->default(1)->after('is_active');
            $table->boolean('registration_open')->default(true)->after('current_semester');
        });
    }

    public function down(): void
    {
        Schema::table('academic_sessions', function (Blueprint $table) {
            $table->dropColumn(['current_semester', 'registration_open']);
        });
    }
};
