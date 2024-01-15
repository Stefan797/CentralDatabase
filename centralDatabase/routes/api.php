<?php

use Illuminate\Http\Request;
// use Illuminate\Support\Facades\Gate;
use App\Http\Controllers\UploadManagerController;
use App\Http\Controllers\FileController;
use App\Http\Controllers\RecipeController;
use App\Http\Controllers\ContactController;
use App\Http\Controllers\BoardController;
use App\Http\Controllers\ChatKIController;
use App\Http\Controllers\IndexcardController;
use App\Http\Controllers\TicketController;
use App\Http\Controllers\ProjectController;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

//   ------ BoardController ------

Route::get('/getUserBoard', [BoardController::class, 'getUserBoard']);
Route::post('/createNewUserTicket', [TicketController::class, 'createNewUserTicket']);

//   ------ ContactController ------

Route::get('/getUserContacts', [ContactController::class, 'getUserContacts']);

//   ------ ChatKIController ------

Route::get('/answer', [ChatKIController::class, 'answer']);

//   ------ FileController ------

Route::get('/getUserFiles', [FileController::class, 'getUserFiles']);
Route::get('/files/getbyfilename/{filename}', [FileController::class, 'getFileByFilename']);
Route::post('/readFileContent', [FileController::class, 'readFileContent']);
Route::post('/updateFileContent', [FileController::class, 'updateFileContent']);
Route::post('/addFurtherTxt', [FileController::class, 'addFurtherTxt']);


//   ------ IndexcardController ------

Route::get('/getUserIndexCards', [IndexcardController::class, 'getUserIndexCards']);

//   ------ ProjectController ------

Route::get('/getUserProjects', [ProjectController::class, 'getUserProjects']);
Route::post('/createNewUserProject', [ProjectController::class, 'createNewUserProject']);

//   ------ RecipeController ------

Route::get('/getAllRecipes', [RecipeController::class, 'getAllRecipes']);

//   ------ UploadManagerController ------

Route::post('/upload', [UploadManagerController::class, 'upload']);





