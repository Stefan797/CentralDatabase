<?php

namespace App\Models;

// use Illuminate\Database\Eloquent\Model;

namespace App\Http\Controllers;

use App\Http\Requests\StoreSearchRequest;
use App\Http\Requests\UpdateSearchRequest;
use App\Models\Search;
use App\Models\File;
use App\Models\Recipe;
use App\Models\User;
use Illuminate\Http\Request;

class SearchController extends Controller
{

    public function search(Request $request)
    {
        $query = $request->input('query');

        $results = [];
        $models = ['File'];

        foreach ($models as $model) {
            $modelClass = "App\\Models\\$model";
            $results[$model] = new $modelClass;
            $results[$model] = $results[$model]->where('filename', 'like', "%$query%")->get();
        }

        return response()->json($results);
    }

    public function searchFileInput(Request $request)
    {
        $query = $request->input('query');

        $results = [];
        $models = ['File'];

        // file_content abspeichern in datenbank wo ? 
        // 

        foreach ($models as $model) {
            $modelClass = "App\\Models\\$model";
            $results[$model] = new $modelClass;

            $results[$model] = $results[$model]->where('filename', 'like', "%$query%")
                ->orWhere(function ($queryBuilder) use ($query) {
                    $queryBuilder->whereRaw("LOWER(file_content) LIKE LOWER(?)", ["%$query%"]);
                })
                ->get();
        }

        return response()->json($results);
    }


    public function searchFileInputExec(Request $request)
    {
        $query = $request->input('query');

        $results = [];
        $models = ['File'];

        foreach ($models as $model) {
            $modelClass = "App\\Models\\$model";
            $results[$model] = new $modelClass;

            $results[$model] = $results[$model]->where('filename', '=', $query)
                ->orWhere(function ($queryBuilder) use ($query) {
                    $queryBuilder->whereRaw("LOWER(file_content) = LOWER(?)", [$query]);
                })
                ->get();
        }

        return response()->json($results);
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
    public function store(StoreSearchRequest $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(Search $search)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Search $search)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateSearchRequest $request, Search $search)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Search $search)
    {
        //
    }
}
