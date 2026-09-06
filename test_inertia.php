<?php
$request = Illuminate\Http\Request::create('/student/registration', 'GET');
$request->setUserResolver(function() { return App\Models\User::find(4); });
$controller = new App\Http\Controllers\Student\DashboardController();
$response = $controller->registration($request);

// The response is an Inertia Response object. We can extract the props.
$props = $response->toResponse($request)->original;
$page = $props->getData(); // This gets the array passed to Inertia view
$availableCourses = $page['page']['props']['availableCourses'];
echo json_encode($availableCourses);
