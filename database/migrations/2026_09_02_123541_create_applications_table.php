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
        Schema::create('applications', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->foreignId('academic_session_id')->constrained();
            $table->foreignId('programme_id')->constrained();
            $table->foreignId('specialisation_id')->nullable()->constrained();
            $table->string('application_number')->unique()->nullable();
            $table->string('status')->default('STARTED');
            $table->json('personal_info')->nullable();
            $table->text('research_concept_note')->nullable();
            $table->timestamps();
            $table->softDeletes();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('applications');
    }
};
