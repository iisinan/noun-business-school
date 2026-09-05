<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('applications', function (Blueprint $table) {
            $table->json('academic_background')->nullable();
            $table->json('olevel_results')->nullable();
            $table->json('employment_info')->nullable();
            $table->json('documents')->nullable();
        });
    }

    public function down(): void
    {
        Schema::table('applications', function (Blueprint $table) {
            $table->dropColumn(['academic_background', 'olevel_results', 'employment_info', 'documents']);
        });
    }
};
