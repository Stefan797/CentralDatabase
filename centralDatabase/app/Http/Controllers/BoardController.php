<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreBoardRequest;
use App\Http\Requests\UpdateBoardRequest;
use App\Models\Board;

class BoardController extends Controller
{

    /**
     * Display a listing of the resource.
     */
    public function getUserBoard()
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
    public function store(StoreBoardRequest $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(Board $board)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Board $board)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateBoardRequest $request, Board $board)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Board $board)
    {
        //
    }
}
