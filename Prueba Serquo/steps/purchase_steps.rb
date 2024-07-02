Given('Login in the application') do
    visit 'https://www.demoblaze.com/'
    fill_in 'username', with: 'data.username'
    fill_in 'password', with: 'data.password'
    click_button 'Login'
    expect(page).to have_current_path('https://www.demoblaze.com/')
  end
  
  When('I add an item to the cart') do
    click_button 'Add to Cart' 
  end
  
  When('I proceed to place order') do
    click_button 'object.placeOrder'
  end
  
  When('I fill in the purchase information') do
    fill_in 'name', with: 'data.name'
    fill_in 'country', with: 'data.country'
    fill_in 'city', with: 'data.city'
    fill_in 'credit card', with: 'data.creditCard'
    fill_in 'month', with: 'data.month'
    fill_in 'year', with: 'data.year'
  end
  
  When('I confirm the purchase') do
    click_button 'Purchase'
  end
  
  Then('I see a confirmation message') do
    expect(page).to_have_content('Thank you for your purchase!')
  end
  
 