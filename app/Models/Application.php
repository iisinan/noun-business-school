<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Application extends Model
{
    protected $guarded = [];

    protected function casts(): array
    {
        return [
            'personal_info' => 'array',
            'academic_background' => 'array',
            'olevel_results' => 'array',
            'employment_info' => 'array',
            'documents' => 'array',
        ];
    }

    public function user() { return $this->belongsTo(User::class); }
    public function programme() { return $this->belongsTo(Programme::class); }
    public function specialisation() { return $this->belongsTo(Specialisation::class); }
    public function payments() { return $this->hasMany(Payment::class); }
    public function academicSession() { return $this->belongsTo(AcademicSession::class); }
}
