<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\File;

class UploadManagerController extends Controller
{
    public function upload(Request $request) {

        if(!auth()->check()) {
            abort(403,'Not logged in!');
        }

        $user = $request->user();

    

        if($request->hasFile('file')){
            // Get filename with the extension
            $filenameWithExt = $request->file('file')->getClientOriginalName();
            //Get just filename
            $filename = pathinfo($filenameWithExt, PATHINFO_FILENAME);
            // Get just ext
            $extension = $request->file('file')->getClientOriginalExtension();
            // Filename to store
            $fileNameToStore = $filename.'.'.$extension; # .time().'.'
            // Upload Image
            $path = $request->file('file')->storeAs('public/files',$fileNameToStore);

            File::create([
                'filename' => $filenameWithExt,
                'filepath' => $path,
                'filetype' => $extension,
                'user_id' => $user->id,
            ]);
        }

        return response()->json([
            'success' => true,
            'uploaded_path' => $path,
            'public_path' => public_path($path)
        ]);
    }
}
