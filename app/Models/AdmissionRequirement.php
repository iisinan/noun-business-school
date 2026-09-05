<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class AdmissionRequirement extends Model
{
    use HasFactory;

    protected $guarded = [];

    public function programme(): BelongsTo
    {
        return $this->belongsTo(Programme::class);
    }

    public function specialisation(): BelongsTo
    {
        return $this->belongsTo(Specialisation::class);
    }
}
