<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;

class AuthController extends Controller
{
    /**
     * Store a newly created resource in storage.
     */
    public function show(Request $request)
    {
        return view('main');
    }

    /**
     * Store a newly created resource in storage.
     */
    public function login(Request $request)
    {
        validator($request->all(), [
            'email' => ['required', 'email'],
            'password' => ['required']
        ])->validate();

        $credentials = $request->only('email', 'password');

        if (auth()->attempt($credentials)) {  #, $request->filled('remember')
            $request->session()->regenerate();
            $user = auth()->user();
            return response()->json([
                'login' => 'success',
                'user' => $user
            ], 200);

            // return [
            //     'token' => $user->createToken(time())->plainTextToken,
            //     'user_id' => $user->id
            // ];
        }

        return response()->json(['error' => 'Unauthorized'], 401);
    }

    /**
     * Logs the user out.
     */
    public function logout(Request $request)
    {
        auth()->logout();
        return response()->json(['logout' => 'success'], 200);
    }
}
