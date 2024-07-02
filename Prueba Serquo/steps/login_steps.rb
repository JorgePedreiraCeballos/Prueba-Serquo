Given('Login in the application') do
    visit 'https://www.demoblaze.com/'
  end

  When('I click on the login button') do
    click_button 'Login'
  end
  
  When('I enter valid credentials') do
    fill_in 'username', with: 'data.username'
    fill_in 'password', with: 'data.password'
    click_button 'Login' button
  end
  
  Then('I am redirected to the home page') do
    expect(page).to_have_current_path('https://www.demoblaze.com/')
  end
  
  Then('I see my user logged') do
    expect(element).to_have_content('Welcome ' + 'data.username')
  end