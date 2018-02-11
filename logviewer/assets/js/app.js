var app = angular.module('logApp', []);


app.controller('mainController', function($scope, $http) {
	// set the default sort values
	$scope.sortType     = 'name'; 
	$scope.sortReverse  = false;
	$scope.searchFish   = '';

	$http({
	    method : "GET",
	    url : "http://localhost:5000/api"
	}).then(function mySuccess(response) {
	    $('div.signal').removeClass('signal');
	    $scope.logs = response.data;
	}, function myError(response) {
	    $scope.logs = response.statusText;
	});
});
