<?php

namespace App\Http\Middleware;

use Illuminate\Http\Request;
use Inertia\Middleware;

class HandleInertiaRequests extends Middleware
{
    /**
     * The root template that is loaded on the first page visit.
     *
     * @var string
     */
    protected $rootView = 'app';

    /**
     * Determine the current asset version.
     */
    public function version(Request $request): ?string
    {
        return parent::version($request);
    }

    /**
     * Define the props that are shared by default.
     *
     * @return array<string, mixed>
     */
    public function share(Request $request): array
    {
        return [
            ...parent::share($request),
            'auth' => [
                'user' => function () use ($request) {
                    $user = $request->user();
                    if ($user) {
                        $data = $user->toArray();
                        $app = \App\Models\Application::where('user_id', $user->id)->latest()->first();
                        if ($app && isset($app->personal_info['passport_photograph_path'])) {
                            $data['passport_url'] = \Illuminate\Support\Facades\Storage::disk('s3')->url($app->personal_info['passport_photograph_path']);
                        }
                        return $data;
                    }
                    return null;
                },
            ],
            'flash' => [
                'success' => $request->session()->get('success'),
                'error' => $request->session()->get('error'),
            ],
        ];
    }
}
