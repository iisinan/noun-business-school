<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Programme extends Model
{
    protected $guarded = [];

    public function specialisations()
    {
        return $this->hasMany(Specialisation::class);
    }

    public function courses()
    {
        return $this->belongsToMany(Course::class);
    }

    public function admissionRequirements()
    {
        return $this->hasMany(AdmissionRequirement::class);
    }
}
