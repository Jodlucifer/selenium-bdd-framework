from behave import given, when, then
import config
from pages.login_page import LoginPage
from pages.project_page import ProjectPage
from pages.video_page import VideoPage


@given('I open the FYC platform')
def step_open_platform(context):
    # Navigate to the platform URL
    context.driver.get(config.BASE_URL)
    # Initialize page objects
    context.login_page = LoginPage(context.driver)
    context.project_page = ProjectPage(context.driver)
    context.video_page = VideoPage(context.driver)


@when('I sign in using PIN')
def step_sign_in(context):
    # Enter PIN and log in
    context.login_page.enter_pin_and_login(config.PIN)


@when('I navigate to the project')
def step_navigate_project(context):
    # Navigate to the specified project
    context.project_page.navigate_to_project(config.PROJECT_NAME)


@when('I switch to Details tab')
def step_switch_details(context):
    # Switch to Details tab
    context.project_page.switch_to_details()


@when('I return to Videos tab')
def step_return_videos(context):
    # Switch back to Videos tab
    context.project_page.switch_to_videos()


@when('I play the video for configured duration and pause')
def step_play_video(context):
    # Play video for configured duration and pause
    context.video_page.play_and_pause_video(config.VIDEO_PLAY_DURATION)


@when('I replay the video using Continue Watching')
def step_continue_watching(context):
    # Replay video using Continue Watching button
    context.video_page.continue_watching()


@when('I set the volume to configured level')
def step_set_volume(context):
    # Set video volume to configured level
    context.video_page.set_volume(config.VOLUME_LEVEL)


@when('I change resolution to configured values')
def step_change_resolution(context):
    # Set the resolution to configured esolution
    context.video_page.change_resolution(config.RESOLUTION_LOW)
    context.video_page.change_resolution(config.RESOLUTION_HIGH)


@when('I pause and exit the project')
def step_pause_exit(context):
    # Pause video and exit project
    context.video_page.pause_video()
    context.project_page.exit_project()


@then('I logout from the platform')
def step_logout(context):
    # Logout from the platform
    context.project_page.logout()
