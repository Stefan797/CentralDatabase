<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Board extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = [
        'project_id',
    ];

    // /**
    //  * Get the post that owns the comment.
    //  */
    // public function user(): BelongsTo
    // {
    //     return $this->belongsTo(User::class);
    // }

    /**
     * Get the post that owns the comment.
     */
    public function project(): BelongsTo
    {
        return $this->belongsTo(Project::class);
    }


    /**
     * Get the post that owns the comment.
     */
    public function tickets(): HasMany
    {
        return $this->hasMany(Ticket::class);
    }


}
