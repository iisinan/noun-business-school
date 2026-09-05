<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('course_registrations', function (Blueprint $table) {
            $table->integer('score')->nullable()->after('status');
            $table->string('grade', 2)->nullable()->after('score');
            $table->integer('grade_points')->nullable()->after('grade');
        });
    }

    public function down(): void
    {
        Schema::table('course_registrations', function (Blueprint $table) {
            $table->dropColumn(['score', 'grade', 'grade_points']);
        });
    }
};
