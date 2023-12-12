<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreChatKIRequest;
use App\Http\Requests\UpdateChatKIRequest;
use App\Models\ChatKI;

class ChatKIController extends Controller
{

    /**
     * Display a listing of the resource.
     */
    public function answer()
    {
        if(!auth()->check()) {
            abort(403,'Not logged in!');
        }

        $user = auth()->user();

        $files = $user->files;

        //$files = File::where('user_id', $user->id)->get();

        //$files = File::all(); // Hole alle Objekte aus der File-Tabelle

        return response()->json([
            'status' => 'success',
            'data' => $files,
        ], 200);
    }

    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreChatKIRequest $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(ChatKI $chatKI)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(ChatKI $chatKI)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateChatKIRequest $request, ChatKI $chatKI)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(ChatKI $chatKI)
    {
        //
    }
}
