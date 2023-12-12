<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreRecipeRequest;
use App\Http\Requests\UpdateRecipeRequest;
use App\Models\Recipe;

class RecipeController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function getAllRecipes()
    {
        $recipes = Recipe::all(); // Hole alle Objekte aus der File-Tabelle

        return response()->json([
            'status' => 'success',
            'data' => $recipes,
        ], 200);
    }

    /**
     * Display a listing of the resource.
     */
    public function getUserRecipes()
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
    public function store(StoreRecipeRequest $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(Recipe $recipe)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Recipe $recipe)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateRecipeRequest $request, Recipe $recipe)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Recipe $recipe)
    {
        //
    }
}
