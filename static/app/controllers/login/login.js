'use strict';

angular.module('XYZ.login', [
  'ui.router',
  'ui.bootstrap',
  'angularMoment'
]).controller('LoginCtrl', function ($scope) {
    $scope.message = {
      time: new Date()
    };
  });
