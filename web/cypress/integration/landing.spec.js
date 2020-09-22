describe('Intro section', () => {
  beforeEach(() => {
    cy.server()
    cy.route('GET', '/plans?zip_code=*').as('getPlans')
  })

  it('returns plans for valid zip codes', () => {
    const zipCode = '75229'

    cy.visit('/')

    cy.get('#intro-section input[type=text]').click().type(zipCode)

    cy.get('#intro-section input[type=text]').should('be.disabled')
    cy.get('#intro-section button').should('not.exist')

    cy.wait('@getPlans').should((xhr) => {
      expect(xhr.status).to.equal(200)
      expect(xhr.response.body).to.be.an('array').that.is.not.empty
    })

    cy.get('#intro-section button').should('exist')

    cy.get('#intro-section input[type=text]').type('{enter}')

    cy.location('pathname').should('eq', `/plans/${zipCode}`)

    cy.get('.plan-card:first')
  })

  it('returns no plans for invalid zip codes', () => {
    const zipCode = '00000'
    const errorMessage = 'No plans found for this zip code'

    cy.visit('/')

    cy.get('#intro-section input[type=text]').click().type(zipCode)

    cy.get('#intro-section input[type=text]').should('be.disabled')
    cy.get('#intro-section button').should('not.exist')

    cy.wait('@getPlans').should((xhr) => {
      expect(xhr.status).to.equal(200)
      expect(xhr.response.body).to.be.an('array').that.is.empty
    })

    cy.get('#intro-section').contains(errorMessage)

    cy.get('#intro-section input[type=text]').type('{enter}')

    cy.location('pathname').should('eq', '/')
  })

  it('alerts on server error', () => {
    cy.route({
      method: 'GET',
      url: '/plans?zip_code=*',
      status: 500,
      response: {},
    }).as('getPlans')

    const alertStub = cy.stub()
    cy.on('window:alert', alertStub)

    const zipCode = '75229'
    const errorMessage = 'Sorry, something went wrong.'

    cy.visit('/')

    cy.get('#intro-section input[type=text]').click().type(zipCode)

    cy.get('#intro-section input[type=text]').should('be.disabled')
    cy.get('#intro-section button').should('not.exist')

    cy.wait('@getPlans').should((xhr) => {
      expect(xhr.status).to.equal(500)
      expect(alertStub).to.be.calledWith(errorMessage)
    })
  })
})

describe('FAQs', () => {
  it('opens one FAQ at a time', () => {
    cy.visit('/')

    cy.get('#faqs .faq-question').eq(0).next().should('not.exist')
    cy.get('#faqs .faq-question').eq(1).next().should('not.exist')

    cy.get('#faqs .faq-question').eq(0).click()

    cy.get('#faqs .faq-question').eq(0).next().should('exist')
    cy.get('#faqs .faq-question').eq(1).next().should('not.exist')

    cy.get('#faqs .faq-question').eq(1).click()

    cy.get('#faqs .faq-question').eq(0).next().should('not.exist')
    cy.get('#faqs .faq-question').eq(1).next().should('exist')
  })
})

describe('Header', () => {
  it('navigates correctly', () => {
    cy.visit('/')

    // FAQs from landing
    cy.get('#header')

    cy.get('#faqs h2').should('not.be.inViewport')

    cy.get('#header').contains('FAQs').click()

    // cy.get('#faqs h2').should('be.inViewport')

    // FAQs from privacy
    cy.visit('/privacy')

    cy.get('#header').contains('FAQs').click()

    cy.location('pathname').should('eq', '/')
    cy.location('hash').should('eq', '#faqs')
    // cy.get('#faqs h2').should('be.inViewport')
  })
})

describe('Footer', () => {
  it('navigates correctly', () => {
    cy.visit('/')

    // FAQs from landing
    cy.get('#footer')

    cy.get('#faqs h2').should('not.be.inViewport')

    cy.get('#footer').contains('FAQs').click()

    cy.get('#faqs h2').should('be.inViewport')

    // privacy from landing
    cy.get('#footer').contains('Privacy').click()

    cy.location('pathname').should('eq', '/privacy')

    // FAQs from privacy
    cy.get('#footer').contains('FAQs').click()

    cy.location('pathname').should('eq', '/')
    cy.location('hash').should('eq', '#faqs')
    cy.get('#faqs h2').should('be.inViewport')

    // terms from landing
    cy.get('#footer').contains('Terms').click()

    cy.location('pathname').should('eq', '/terms')

    // landing from terms
    cy.get('#footer').contains('Home').click()

    cy.location('pathname').should('eq', '/')
  })
})
