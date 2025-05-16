Feature: Iot Dashboard Scenarios

  Scenario: Verify the Iot Dashboard Page Card Status
    Given I open the url "http://localhost:4200/"
    And I verify the IotDashboardPage loaded
    And I verify lightCard status is ON
    And I verify rollerShadesCard status is ON
    And I verify wirelessAudioCard status is ON
    And I verify coffeeMakerCard status is ON