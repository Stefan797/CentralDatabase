<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreProjectRequest;
use App\Http\Requests\UpdateProjectRequest;
use App\Models\Project;
use Illuminate\Http\Request;

class ProjectController extends Controller
{

    /**
     * Display a listing of the resource.
     */
    public function getUserProjects()
    {
        if (!auth()->check()) {
            abort(403, 'Not logged in!');
        }

        $user = auth()->user();
        $projects = $user->projects;

        return response()->json([
            'status' => 'success',
            'data' => $projects,
        ], 200);
    }

    /**
     * Display a listing of the resource.
     */
    public function createNewUserProject(Request $request)
    {
        // if (!auth()->check()) {
        //     abort(403, 'Not logged in!');
        // }

        // $validatedData = $request->validate([
        //     'name' => 'required|string|max:255',
        // ]);

        // $project = Project::create([
        //     'name' => $validatedData['name'],
        // ]);

        $user_id = auth()->id();

        $project = Project::create([
            'name' => $request->get('name'),
            'user_id' => $user_id,
        ]);

        #return response()->json($project, 201);
        
        return response()->json([
            'status' => 'success',
            'data' => $project,
        ], 201);
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
    public function store(StoreProjectRequest $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(Project $project)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Project $project)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateProjectRequest $request, Project $project)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Project $project)
    {
        //
    }
}
