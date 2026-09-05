<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class CourseRegistration extends Model
{
    protected $fillable = ['user_id', 'academic_session_id', 'semester', 'course_id', 'amount', 'status'];

    public function user()
    {
        return $this->belongsTo(User::class);
    }

    public function academicSession()
    {
        return $this->belongsTo(AcademicSession::class);
    }

    public function course()
    {
        return $this->belongsTo(Course::class);
    }
}
