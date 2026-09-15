<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SemesterRegistration extends Model
{
    protected $fillable = ['user_id', 'academic_session_id', 'school_semester', 'semester', 'amount', 'status', 'is_summer'];

    public function user()
    {
        return $this->belongsTo(User::class);
    }

    public function academicSession()
    {
        return $this->belongsTo(AcademicSession::class);
    }
}
