Feature: Automate FYC Platform Tasks

  Scenario: Automate video playback and settings
    Given I open the FYC platform
    When I sign in using PIN
    And I navigate to the project
    And I switch to Details tab
    And I return to Videos tab
    And I play the video for configured duration and pause
    And I replay the video using Continue Watching
    And I set the volume to configured level
    And I change resolution to configured values
    And I pause and exit the project
    Then I logout from the platform