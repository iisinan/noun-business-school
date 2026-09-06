<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::table('applications', function (Blueprint $table) {
            $table->index('user_id');
            $table->index('programme_id');
            $table->index('academic_session_id');
            $table->index('status');
            $table->index('created_at');
        });

        Schema::table('payments', function (Blueprint $table) {
            $table->index('user_id');
            $table->index('application_id');
            $table->index('status');
            $table->index('created_at');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('applications', function (Blueprint $table) {
            $table->dropIndex(['user_id']);
            $table->dropIndex(['programme_id']);
            $table->dropIndex(['academic_session_id']);
            $table->dropIndex(['status']);
            $table->dropIndex(['created_at']);
        });

        Schema::table('payments', function (Blueprint $table) {
            $table->dropIndex(['user_id']);
            $table->dropIndex(['application_id']);
            $table->dropIndex(['status']);
            $table->dropIndex(['created_at']);
        });
    }
};
