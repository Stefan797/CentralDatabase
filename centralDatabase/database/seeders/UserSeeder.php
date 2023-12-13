<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\User;
use Illuminate\Support\Facades\Hash;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        User::create([
            'username' => 'TestNutzer1',
            'first_name' => 'Test',
            'last_name' => 'Nutzer',
            'email' => 'test@t.de',
            'password' => Hash::make('test'),
        ]);

        User::create([
            'username' => 'CentralDatabaseAdmin1',
            'first_name' => 'Stefan',
            'last_name' => 'Hübner',
            'email' => 'Stefan.huebner97@web.de',
            'password' => Hash::make('password2'),
        ]);
    }
}