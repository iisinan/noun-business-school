<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Specialisation extends Model
{
    protected $guarded = [];

    public function programme()
    {
        return $this->belongsTo(Programme::class);
    }

    public function courses()
    {
        return $this->belongsToMany(Course::class)->withPivot('is_elective');
    }

    public function admissionRequirements()
    {
        return $this->hasMany(AdmissionRequirement::class);
    }
}
