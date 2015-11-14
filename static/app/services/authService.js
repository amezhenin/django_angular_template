angular.module('XYZ.authService', [])

  .factory("authService", [
    '$http', '$q', '$state',
    function ($http, $q, $state) {

      var service = {};


      service.login = function (username, password) {
        var deferred = $q.defer();

        $http.post("/api/login", {
          username: username,
          password: password
        }).then(function (result) {
          deferred.resolve(result.data);
        }, function (error) {
          deferred.reject(error);
        });

        return deferred.promise;
      };


      service.logout = function(){
        $http.post("/api/logout", {})
          .then(function(){
            $state.go('login');
          })
      };


      service.isLoggedIn = function(){
        return $http.get("/api/login");
      };


      return service;
    }]);