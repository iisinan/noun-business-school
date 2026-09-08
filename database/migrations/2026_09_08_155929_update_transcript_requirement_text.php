<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;
use Illuminate\Support\Facades\DB;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        DB::table('admission_requirements')
            ->where('description', 'like', '%academic transcripts and certificates from previously attended institutions%')
            ->update([
                'description' => 'Student copy of academic transcripts and certificates from previously attended institutions.',
            ]);
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        DB::table('admission_requirements')
            ->where('description', 'Student copy of academic transcripts and certificates from previously attended institutions.')
            ->update([
                'description' => 'Certified copies of academic transcripts and certificates from previously attended institutions.',
            ]);
    }
};
