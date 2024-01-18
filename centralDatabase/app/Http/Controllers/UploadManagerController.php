<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\File;
use Illuminate\Support\Facades\Storage;

class UploadManagerController extends Controller
{
    public function upload(Request $request)
    {

        if (!auth()->check()) {
            abort(403, 'Not logged in!');
        }

        $user = $request->user();



        if ($request->hasFile('file')) {
            // Get filename with the extension
            $filenameWithExt = $request->file('file')->getClientOriginalName();
            //Get just filename
            $filename = pathinfo($filenameWithExt, PATHINFO_FILENAME);
            // Get just ext
            $extension = $request->file('file')->getClientOriginalExtension();
            // Filename to store
            $fileNameToStore = $filename . '.' . $extension; # .time().'.'

            // Überprüfen, ob der Dateiname bereits existiert
            if (Storage::disk('public')->exists("files/{$fileNameToStore}")) {
                return response()->json([
                    'success' => false,
                    'error' => 'Dateiname existiert bereits. Bitte wählen Sie einen anderen Dateinamen.',
                ]);
            }

            // Upload Image
            $path = $request->file('file')->storeAs('public/files', $fileNameToStore);

            // Überprüfen Sie, ob die Datei erfolgreich hochgeladen wurde
            if ($path) {
                // Set File Content From File
                $content = Storage::disk('public')->get("files/{$fileNameToStore}");

                File::create([
                    'filename' => $filenameWithExt,
                    'file_content' => $content,
                    'filepath' => $path,
                    'filetype' => $extension,
                    'user_id' => $user->id,
                ]);
            }
        }

        return response()->json([
            'success' => true,
            'uploaded_path' => $path,
            'public_path' => public_path($path)
        ]);
    }


    // public function upload(Request $request) {

    //     if(!auth()->check()) {
    //         abort(403,'Not logged in!');
    //     }

    //     $user = $request->user();



    //     if($request->hasFile('file')){
    //         // Get filename with the extension
    //         $filenameWithExt = $request->file('file')->getClientOriginalName();
    //         //Get just filename
    //         $filename = pathinfo($filenameWithExt, PATHINFO_FILENAME);
    //         // Get just ext
    //         $extension = $request->file('file')->getClientOriginalExtension();
    //         // Filename to store
    //         $fileNameToStore = $filename.'.'.$extension; # .time().'.'
    //         // Upload Image
    //         $path = $request->file('file')->storeAs('public/files',$fileNameToStore);

    //         // Set File Content From File
    //         $content = Storage::disk('public')->get("files/{$filename}");

    //         File::create([
    //             'filename' => $filenameWithExt,
    //             'file_content' => $content,
    //             'filepath' => $path,
    //             'filetype' => $extension,
    //             'user_id' => $user->id,
    //         ]);
    //     }

    //     return response()->json([
    //         'success' => true,
    //         'uploaded_path' => $path,
    //         'public_path' => public_path($path)
    //     ]);
    // }
}
