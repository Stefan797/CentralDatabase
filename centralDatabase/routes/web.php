<?php

#use App\Http\Controllers\EmployeeController;

use App\Http\Controllers\AuthController;
// use App\Http\Controllers\UploadManagerController;
use App\Http\Controllers\UserController;
use Illuminate\Support\Facades\Route;

// use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/v/login', function () {
    return view('main');
})->name('login');

Route::middleware('auth:sanctum')->get('/v/{vue_capture?}', function () {
    return view('main');
})->where('vue_capture', '[\/\w\.-]*');

#Route::get('/v', 'AuthController')->middleware('auth');

Route::post('/user/create', [UserController::class, 'register']); 

Route::post('/user/login', [AuthController::class, 'login']);

Route::get('/user/logout', [AuthController::class, 'logout']);

// Route::get('/upload', [UploadManagerController::class, 'upload'])->name('upload');
// Route::post('/uploadS', [UploadManagerController::class, 'uploadPost'])->name('upload.post');

#Route::get('/', [AuthController::class, 'logout']); Andere Pfade die nicht exsistieren 

#Route::post('/employee/create', [EmployeeController::class, 'store']); Für Mitarbeiter