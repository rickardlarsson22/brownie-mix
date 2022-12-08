// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity 0.7.3;

contract YourContract {
    uint256 number;

    function setNumber(uint256 _num) public {
        number = _num;
    }

    function getNumber() public view returns (uint256) {
        return number;
    }
}
