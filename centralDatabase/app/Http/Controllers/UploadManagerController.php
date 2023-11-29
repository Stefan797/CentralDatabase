<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class UploadManagerController extends Controller
{
    public function upload(Request $request) {

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
        }

        return response()->json([
            'success' => true,
            'uploaded_path' => $path,
            'public_path' => public_path($path)
        ]);
    }
}
