<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
// use Illuminate\Support\Facades\Auth;
// use Illuminate\Support\Facades\Hash;
// use Illuminate\Support\Str;
// use Laravel\Passport\Passport;

class UserController extends Controller
{
    public function register(Request $request)
    {
        $data = $request->all();
        $user = User::create($data);
        $token = $user->createToken('Personal Access Token')->accessToken;

        return response()->json([
            'status' => 'success',
            'data' => $user,
            'access_token' => $token
        ], 200);
    }
}
