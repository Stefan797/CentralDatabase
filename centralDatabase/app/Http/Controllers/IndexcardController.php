<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreIndexcardRequest;
use App\Http\Requests\UpdateIndexcardRequest;
use App\Models\Indexcard;

class IndexcardController extends Controller
{

    /**
     * Display a listing of the resource.
     */
    public function getUserIndexcards()
    {
        if(!auth()->check()) {
            abort(403,'Not logged in!');
        }

        $user = auth()->user();
        $files = $user->files;

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
    public function store(StoreIndexcardRequest $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(Indexcard $indexcard)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Indexcard $indexcard)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateIndexcardRequest $request, Indexcard $indexcard)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Indexcard $indexcard)
    {
        //
    }
}
