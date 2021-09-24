export const termOptions = ['All', 1, 3, 6, 12, 18, 24, 36] as const

export interface Tdu {
  name: string
}

export interface Provider {
  name: string
  is_active: boolean
  rating: number
}

export interface Plan {
  tdu: Tdu
  provider: Provider
  name: string
  is_active: boolean
  low_usage_rate: string
  medium_usage_rate: string
  high_usage_rate: string
  is_new_customer: boolean
  percent_renewable: number
  term: number
  language: string
  terms_url: string
  facts_url: string
  enroll_url: string
  enroll_phone: string
}
