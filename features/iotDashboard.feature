Feature: Iot Dashboard Scenarios

  Scenario Outline: Verify the Iot Dashboard Page Card Status
    Given I open the url "http://localhost:4200/"
    And I verify <card> status is ON

    Examples:
      | card              |
      | lightCard         |
      | rollerShadesCard  |
      | wirelessAudioCard |
      | coffeeMakerCard   |


  Scenario Outline: Interact Iot Dashboard Page Card and verify Status
    Given I open the url "http://localhost:4200/"
    And I verify <card> status is ON
    When I click on <card>
    Then I verify <card> status is OFF

    Examples:
    | card              |
    | lightCard         |
    | rollerShadesCard  |
    | wirelessAudioCard |
    | coffeeMakerCard   |