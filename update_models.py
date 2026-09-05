import os

# Update User.php
user_file = "app/Models/User.php"
with open(user_file, "r") as f:
    content = f.read()

# Add wallet_balance to fillables
content = content.replace("#[Fillable(['first_name', 'middle_name', 'last_name', 'phone', 'email', 'password'])]", "#[Fillable(['first_name', 'middle_name', 'last_name', 'phone', 'email', 'password', 'wallet_balance'])]")

# Add relationships
relationships = """
    public function applications()
    {
        return $this->hasMany(Application::class);
    }

    public function walletTransactions()
    {
        return $this->hasMany(WalletTransaction::class);
    }

    public function semesterRegistrations()
    {
        return $this->hasMany(SemesterRegistration::class);
    }

    public function courseRegistrations()
    {
        return $this->hasMany(CourseRegistration::class);
    }
"""
content = content.replace("""    public function applications()
    {
        return $this->hasMany(Application::class);
    }""", relationships)

with open(user_file, "w") as f:
    f.write(content)

# Update WalletTransaction.php
wt_file = "app/Models/WalletTransaction.php"
wt_content = """<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class WalletTransaction extends Model
{
    protected $fillable = ['user_id', 'type', 'amount', 'description', 'reference_id'];

    public function user()
    {
        return $this->belongsTo(User::class);
    }
}
"""
with open(wt_file, "w") as f:
    f.write(wt_content)

# Update SemesterRegistration.php
sr_file = "app/Models/SemesterRegistration.php"
sr_content = """<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SemesterRegistration extends Model
{
    protected $fillable = ['user_id', 'academic_session_id', 'amount', 'status'];

    public function user()
    {
        return $this->belongsTo(User::class);
    }

    public function academicSession()
    {
        return $this->belongsTo(AcademicSession::class);
    }
}
"""
with open(sr_file, "w") as f:
    f.write(sr_content)

# Update CourseRegistration.php
cr_file = "app/Models/CourseRegistration.php"
cr_content = """<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class CourseRegistration extends Model
{
    protected $fillable = ['user_id', 'academic_session_id', 'course_id', 'amount', 'status'];

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
"""
with open(cr_file, "w") as f:
    f.write(cr_content)

print("Models updated.")
