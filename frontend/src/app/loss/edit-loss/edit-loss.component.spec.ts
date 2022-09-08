/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { EditLossComponent } from './edit-loss.component';

describe('EditLossComponent', () => {
  let component: EditLossComponent;
  let fixture: ComponentFixture<EditLossComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EditLossComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EditLossComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
