<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class AcademicSession extends Model
{
    protected $guarded = [];

    protected $casts = [
        'is_active' => 'boolean',
        'registration_open' => 'boolean',
    ];

    public function applications()
    {
        return $this->hasMany(Application::class);
    }
}