<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Referee extends Model
{
    protected $fillable = [
        'application_id', 'name', 'email', 'phone', 'organisation', 'token', 'status', 'reference_content'
    ];

    public function application()
    {
        return $this->belongsTo(Application::class);
    }
}
