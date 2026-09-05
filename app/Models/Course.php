<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Course extends Model
{
    use HasFactory;

    protected $guarded = [];

    public function programmes(): BelongsToMany
    {
        return $this->belongsToMany(Programme::class);
    }

    public function specialisations(): BelongsToMany
    {
        return $this->belongsToMany(Specialisation::class)->withPivot('is_elective');
    }
}
