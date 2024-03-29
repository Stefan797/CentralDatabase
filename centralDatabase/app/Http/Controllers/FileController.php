<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Http\Requests\StoreFileRequest;
use App\Http\Requests\UpdateFileRequest;
use App\Models\File;
use Illuminate\Support\Facades\Storage;

class FileController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function getAllFiles()
    {
        $files = File::all(); // Hole alle Objekte aus der File-Tabelle

        return response()->json([
            'status' => 'success',
            'data' => $files,
        ], 200);
    }

    /**
     * Display a listing of the resource.
     */
    public function getUserFiles()
    {
        if (!auth()->check()) {
            abort(403, 'Not logged in!');
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
     * Get a file by its filename.
     *
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function getFileByFilename(Request $request, $filename)
    {
        // $filename = $request->input('filename');
        // echo $filename;

        // ddd($filename);

        // Suche die Datei anhand des Dateinamens
        $file = File::where('filename', $filename)->first();

        if ($file) {
            return response()->json([
                'status' => 'success',
                'data' => $file,
            ], 200);
        } else {
            return response()->json([
                'status' => 'error',
                'message' => 'Datei nicht gefunden',
            ], 404);
        }
    }

    public function readFileContent(Request $request)
    {
        $filename = $request->input('filename');

        // dd($filename);

        if (Storage::disk('public')->exists("files/{$filename}")) {
            $content = Storage::disk('public')->get("files/{$filename}");
            // dd($content);
            // Hier können Sie den Inhalt der Datei weiterverarbeiten
            return response()->json([
                'status' => 'success',
                'data' => $content,
            ], 200);
        } else {
            // Datei existiert nicht
            return "Die Datei '{$filename}' existiert nicht.";
        }
    }

    public function updateFileContent(Request $request)
    {
        $filename = $request->input('filename');

        if (Storage::disk('public')->exists("files/{$filename}")) {
            
            $newContent = $request->input('filecontent');
    
            Storage::disk('public')->put("files/{$filename}", $newContent);
    
            return response()->json([
                'status' => 'success',
                'message' => 'Dateiinhalt erfolgreich aktualisiert.',
            ], 200);
        } else {
            // Datei existiert nicht
            return response()->json([
                'status' => 'error',
                'message' => "Die Datei '{$filename}' existiert nicht.",
            ], 404);
        }
    }

    public function addFurtherTxt(Request $request)
    {
        $filename = $request->input('filename');
        $message = $request->input('message');

        if ($message !== null) { # && is_string($message)
            $filePath = 'public/files/' . $filename;

            // Füge die Nachricht zur Datei hinzu
            Storage::append($filePath, $message);

            return response()->json([
                'status' => 'success',
            ], 200);
        } else {
            return response()->json([
                'status' => 'error',
                'message' => 'Ungültige Nachricht.',
            ], 400);
        }
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
    public function store(StoreFileRequest $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(File $file)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(File $file)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateFileRequest $request, File $file)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(File $file)
    {
        //
    }
}
