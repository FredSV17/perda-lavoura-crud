/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { ListLossComponent } from './list-loss.component';

describe('ListLossComponent', () => {
  let component: ListLossComponent;
  let fixture: ComponentFixture<ListLossComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListLossComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListLossComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
