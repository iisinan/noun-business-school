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
        Schema::create('fee_structures', function (Blueprint $table) {
            $table->id();
            $table->foreignId('academic_session_id')->constrained();
            $table->foreignId('programme_id')->constrained();
            $table->foreignId('specialisation_id')->nullable()->constrained();
            $table->integer('level')->nullable();
            $table->integer('semester')->nullable();
            $table->string('fee_type');
            $table->decimal('amount', 12, 2);
            $table->boolean('is_mandatory')->default(true);
            $table->boolean('is_active')->default(true);
            $table->timestamps();
            $table->softDeletes();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('fee_structures');
    }
};
