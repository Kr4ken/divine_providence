"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require("@angular/core");
var interest_service_1 = require("../interestService/interest.service");
var CompleteComponent = (function () {
    function CompleteComponent(interestService) {
        this.interestService = interestService;
        this.interestList = [];
    }
    CompleteComponent.prototype.getInterests = function () {
        var _this = this;
        // this.interestList = this.interestService.getInterestsTest();
        this.interestService
            .getInterests()
            .then(function (interests) { _this.interestList = interests; _this.selectedInterest = _this.interestList[0]; });
    };
    CompleteComponent.prototype.findInterestIndex = function (interest) {
        for (var i = this.interestList.length - 1; i >= 0; i--) {
            if (this.interestList[i] == this.selectedInterest) {
                return i;
            }
        }
        return -1;
    };
    CompleteComponent.prototype.completeInterest = function () {
        var _this = this;
        this.interestService
            .completeInterest(this.selectedInterest.list_key)
            .then(function (interest) {
            _this.interestList[_this.findInterestIndex(_this.selectedInterest)] = interest;
            _this.selectedInterest = interest;
        });
    };
    CompleteComponent.prototype.ngOnInit = function () {
        this.getInterests();
    };
    CompleteComponent.prototype.onSelect = function (interest) {
        this.selectedInterest = interest;
    };
    return CompleteComponent;
}());
CompleteComponent = __decorate([
    core_1.Component({
        selector: 'complete',
        templateUrl: 'ng/app/complete/complete.component.html'
    }),
    __metadata("design:paramtypes", [interest_service_1.InterestService])
], CompleteComponent);
exports.CompleteComponent = CompleteComponent;
//# sourceMappingURL=complete.component.js.map